from bs4 import BeautifulSoup
import pandas as pd
import requests

page_url = "https://test-smell-catalog.readthedocs.io/en/latest/Code%20related/index.html"

non_smells = ["Code duplication", "Complex - Hard to understand", "In association with production code",
              "Mock and stub related", "Violating coding best practices"]


def remove_non_smells(array):
    """
      Remove the non smells link
    """
    filtered_result = filter(lambda x: x not in non_smells, array)
    result_list = sorted(filtered_result)
    return result_list


def convert_to_csv(array):
    """
      Convert the array in a csv file
    """
    data_frame = pd.DataFrame(array)
    data_frame.to_csv("smells.csv")
    print("CSV GENERATED.......")


def get_smells_strings(all_smells):
    """
      Get smells strings
    """
    result = []
    for element in all_smells:
        result.append(element.string)
    return result


def get_data():
    """
        Get data from the page
    """
    html = requests.get(page_url).content
    soup = BeautifulSoup(html, 'html.parser')
    all_smells = soup.findAll("a", class_="reference internal")
    result = get_smells_strings(all_smells)
    filtered_data = remove_non_smells(result)
    convert_to_csv(filtered_data)



get_data()
