# Name: ...
# CodeFellows Python F2: SEA-C42
# Homework 14: Election prediction

import csv
# import os
import time


def read_csv(path):
    """
    Reads the CSV file at path, and returns a list of rows. Each row is a
    dictionary that maps a column name to a value in that column, as a string.
    """
    output = []
    for row in csv.DictReader(open(path)):
        output.append(row)
    return output


################################################################################
# Problem 1: State edges
################################################################################

def row_to_edge(row):
    """
    Given an *ElectionDataRow* or *PollDataRow*, returns the
    Democratic *Edge* in that *State*.
    """
    return float(row["Dem"]) - float(row["Rep"])


def state_edges(election_result_rows):
    """
    Given a list of *ElectionDataRow*s, returns *StateEdge*s.
    The input list has no duplicate *States*;
    that is, each *State* is represented at most once in the input list.
    """
    d = {}
    for row in election_result_rows:
        state = row['State']
        dem = row['Dem']
        rep = row['Rep']
        d[state] = float(dem) - float(rep)
    return d


################################################################################
# Problem 2: Find the most recent poll row
################################################################################

def earlier_date(date1, date2):
    """
    Given two dates as strings (formatted like "Oct 06 2012"), returns True if
    date1 is before date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))


def most_recent_poll_row(poll_rows, pollster, state):
    """
    Given a list of *PollDataRow*s, returns the most recent row with the
    specified *Pollster* and *State*. If no such row exists, returns None.
    """
    mostRecentDate = 'Jan 01 1900'
    d = {}
    for poll_data_row in poll_rows:
        statePoll = poll_data_row["State"]
        datePoll = poll_data_row["Date"]
        pollsterPoll = poll_data_row["Pollster"]
        if (pollster == pollsterPoll and state == statePoll):
            if (earlier_date(mostRecentDate, datePoll)):
                mostRecentDate = datePoll
                d = poll_data_row
    if (d):
        return d
    else:
        return None


################################################################################
# Problem 3: Pollster predictions
################################################################################

def unique_column_values(rows, column_name):
    """
    Given a list of rows and the name of a column (a string),
    returns a set containing all values in that column.
    """
    d = {}
    for row in rows:
        value = row[column_name]
        d.setdefault(value, None)
    return d.keys()


def pollster_predictions(poll_rows):
    """
    Given a list of *PollDataRow*s, returns *PollsterPredictions*.
    For a given pollster, uses only the most recent poll for a state.
    """
    d = {}
    for poll_data_row in poll_rows:
        state = poll_data_row["State"]
        pollster = poll_data_row["Pollster"]

        recent_row = most_recent_poll_row(poll_rows, pollster, state)
        dem = recent_row["Dem"]
        rep = recent_row["Rep"]

        if pollster not in d:
            d[pollster] = {}
        d[pollster][state] = float(dem) - float(rep)
    return d


################################################################################
# Problem 4: Pollster errors
################################################################################

def average_error(state_edges_predicted, state_edges_actual):
    """
    Given predicted *StateEdges* and actual *StateEdges*, returns
    the average error of the prediction.
    """
    stateCount = 0
    diffSum = 0
    for state in state_edges_predicted:
        stateCount += 1
        diffSum += abs(state_edges_predicted[state] - state_edges_actual[state])
    aveError = diffSum / stateCount
    return aveError


def pollster_errors(pollster_predictions, state_edges_actual):
    """
    Given *PollsterPredictions* and actual *StateEdges*,
    retuns *PollsterErrors*.
    """
    d = {}
    for pollster in pollster_predictions:
        aveErr = average_error(pollster_predictions[pollster],
                               state_edges_actual)
        d[pollster] = aveErr
    return d


################################################################################
# Problem 5: Pivot a nested dictionary
################################################################################

def pivot_nested_dict(nested_dict):
    """
    Pivots a nested dictionary, producing a different nested dictionary
    containing the same values.
    The input is a dictionary d1 that maps from keys k1 to dictionaries d2,
    where d2 maps from keys k2 to values v.
    The output is a dictionary d3 that maps from keys k2 to dictionaries d4,
    where d4 maps from keys k1 to values v.
    For example:
      input = { "a" : { "x": 1, "y": 2 },
                "b" : { "x": 3, "z": 4 } }
      output = {'y': {'a': 2},
                'x': {'a': 1, 'b': 3},
                'z': {'b': 4} }
    """
    d = {}
    for key in nested_dict:
        insideDict = nested_dict[key]
        for insideKey in insideDict:
            value = nested_dict[key][insideKey]
            if insideKey not in d:
                d[insideKey] = {}
            d[insideKey][key] = value
    return d


################################################################################
# Problem 6: Average the edges in a single state
################################################################################

def average_error_to_weight(error):
    """
    Given the average error of a pollster, returns that pollster's weight.
    The error must be a positive number.
    """
    return error ** (-2)

# The default average error of a pollster who did no polling in the
# previous election.
DEFAULT_AVERAGE_ERROR = 5.0


def pollster_to_weight(pollster, pollster_errors):
    """"
    Given a *Pollster* and a *PollsterErrors*,
    return the given pollster's weight.
    """
    if pollster not in pollster_errors:
        weight = average_error_to_weight(DEFAULT_AVERAGE_ERROR)
    else:
        weight = average_error_to_weight(pollster_errors[pollster])
    return weight


def weighted_average(items, weights):
    """
    Returns the weighted average of a list of items.

    Arguments:
    items is a list of numbers.
    weights is a list of numbers, whose sum is nonzero.

    Each weight in weights corresponds to the item in items at the same index.
    items and weights must be the same length.
    """
    assert len(items) > 0
    assert len(items) == len(weights)
    numer = 0
    for i in range(len(items)):
        numer += items[i] * weights[i]
    wtdAve = numer / sum(weights)
    return wtdAve


def average_edge(pollster_edges, pollster_errors):
    """
    Given *PollsterEdges* and *PollsterErrors*, returns the average
    of these *Edge*s weighted by their respective *PollsterErrors*.
    """
    edges = []
    weights = []
    for pollster in pollster_edges:
        weight = pollster_to_weight(pollster, pollster_errors)
        edges.append(pollster_edges[pollster])
        weights.append(weight)
    return weighted_average(edges, weights)


################################################################################
# Problem 7: Predict the 2012 election
################################################################################

def predict_state_edges(pollster_predictions, pollster_errors):
    """
    Given *PollsterPredictions* from a current election and
    *PollsterErrors* from a past election,
    returns the predicted *StateEdges* of the current election.
    """
    stateEdges = {}

    pivot_pollster_predictions = pivot_nested_dict(pollster_predictions)

    for state in pivot_pollster_predictions:
        aveEdge = average_edge(pivot_pollster_predictions[state],
                               pollster_errors)
        stateEdges[state] = aveEdge

    return stateEdges



################################################################################
# Electoral College, Main Function, etc.
################################################################################

def electoral_college_outcome(ec_rows, state_edges):
    """
    Given electoral college rows and state edges, returns the outcome of
    the Electoral College, as a map from "Dem" or "Rep" to a number of
    electoral votes won.  If a state has an edge of exactly 0.0, its votes
    are evenly divided between both parties.
    """
    ec_votes = {}               # maps from state to number of electoral votes
    for row in ec_rows:
        ec_votes[row["State"]] = float(row["Electors"])

    outcome = {"Dem": 0, "Rep": 0}
    for state in state_edges:
        votes = ec_votes[state]
        if state_edges[state] > 0:
            outcome["Dem"] += votes
        elif state_edges[state] < 0:
            outcome["Rep"] += votes
        else:
            outcome["Dem"] += votes/2.0
            outcome["Rep"] += votes/2.0
    return outcome


def print_dict(dictionary):
    """
    Given a dictionary, prints its contents in sorted order by key.
    Rounds float values to 8 decimal places.
    """
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if type(value) == float:
            value = round(value, 8)
        print(key, value)


def main():
    """
    Main function, which is executed when election.py is run as a Python script.
    """
    # Read state edges from the 2008 election
    edges_2008 = state_edges(read_csv("data/2008-results.csv"))

    # Read pollster predictions from the 2008 and 2012 election
    polls_2008 = pollster_predictions(read_csv("data/2008-polls.csv"))
    polls_2012 = pollster_predictions(read_csv("data/2012-polls.csv"))

    # Compute pollster errors for the 2008 election
    error_2008 = pollster_errors(polls_2008, edges_2008)

    # Predict the 2012 state edges
    prediction_2012 = predict_state_edges(polls_2012, error_2008)

    # Obtain the 2012 Electoral College outcome
    ec_2012 = electoral_college_outcome(read_csv("data/2012-electoral-college.csv"),
                                        prediction_2012)

    print("Predicted 2012 election results:")
    print_dict(prediction_2012)
    print()

    print("Predicted 2012 Electoral College outcome:")
    print_dict(ec_2012)
    print()


# If this file, election.py, is run as a Python script (such as by typing
# "python election.py" at the command shell), then run the main() function.
if __name__ == "__main__":
    main()


###
### Collaboration
###

# No one helped with the assignment
