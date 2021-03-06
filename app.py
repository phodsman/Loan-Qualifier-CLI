# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import sys
import fire
import questionary
from pathlib import Path
from pathlib import PurePath

from qualifier.utils.fileio import load_csv, save_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file. Uses the questionary path function for auto-fill to increase ease of entry.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.path("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered


def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file. Exits if there are no qualifying loans or if the user declines to save. Alerts the user if the path entered does not exist and asks if the user would like to create the folder entered. Exits if the user declines, otherwise creates the folder and writes to file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # Exits if there are no qualifying loans and informs user
    if len(qualifying_loans) == 0:
        sys.exit("There are no qualifying loans to save to file.")
    
    # Queries user and exits without saving if user does not wish to save.
    want_to_save = questionary.confirm("Save the list of qualifying loans to file?").ask()
    if want_to_save == False:
        sys.exit("Exiting without saving.")

    # Asks user where to save and extracts the directory from the path entered.
    csvpath = questionary.text("Enter a file path to output the qualifying loans (.csv):").ask()
    csvpath_directory = Path(csvpath).parents[0]
    
    # Checks if the directory exists, if not queries user if they wish to create it and does so if they agree.
    if not csvpath_directory.exists():
        create_directory_query = questionary.confirm(f"Folder {csvpath_directory} does not exist. Create folder and save?").ask()
        if create_directory_query == False:
            sys.exit()
        Path.mkdir(csvpath_directory)

    # Saves qualifying loans in path specified and informs user.
    csvpath = Path(csvpath)
    save_csv(csvpath, qualifying_loans)
    print(f"Qualifying loans information saved in {csvpath}")


def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
