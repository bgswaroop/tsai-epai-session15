# EPAi session15 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.7.4 \
Python packages  :   refer to requirements.txt

---
## Session15 objectives
This assignment, helps to code the concepts that are learnt in the session 15 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 

- Yielding and Generator Functions
- Making an iterable from a Generator
- Generator Expressions and Performance
- Yield From
- Aggregators
- Slicing
- Selecting and Filtering
- Infinite Iterators
- Chaining and Teeing
- Mapping and Reduction
- Zipping
 
---

The test cases can be executed by executing _pytest_, from python shell
 
---

### Functions


**fetch_data()**

    Goal 1
    Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate
    - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer,
    then it should be stored as an integer, etc.
     : return :  generator that returns single ticket at a time

**compute_violations_by_car_make()**

    Goal 2
    Calculate the number of violations by car make.
     : return :  A dictionary containing the violations per car make

**print_data()**

    Print the entire data
     : return : 


---

### Unit Tests


**test_readme_exists()**

    Check if the README file exists
     : return :  None

**test_readme_contents()**

    Test the length of the README file
     : return :  None

**test_readme_file_for_formatting()**

    Tests the formatting for the README file
     : return :  None

**test_function_name_had_cap_letter()**

    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
     : return :  None

**test_fetch_data()**

    Try exhausting the generator
     : return :  None

**test_compute_violations_by_car()**

    Test the number of violations by car brand
     : return :  None

---

#### 