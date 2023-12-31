DO NOT COMMIT THE OPENAI API KEY. See "Task 4 GPT Text Extraction" item #4.

# General (you will need to work with other Tasks to complete these)
1. The MongoDB connection string should be drawn from a consistent source for all tasks (so it only needs to be defined once). Task 1 uses an OS-level environment variable. This might work for your task!
2. Add ALL requirements for all tasks into a file named `requirements.txt` such that it can be installed using `pip install -r requirements.txt`.
3. A general comment on in-line documentation: You didn't need to comment on literally every line saying what the line is doing. That's just lazy and readers of your code will not enjoy it. You only need to comment on lines where it's unclear _why_ you did what you did, such as the random `sleep` statement we added to fix OpenAI's issue.

# Task 4 Runner Code Comments
1. Use global constants when referring to DataFrame columns, e.g. `df[FIELD_NAME]` instead of `df['Field Name ']`.
2. In `checkFieldName`, can just `return len(filtered_df) > 0 or ...`. In general, `if cond: return True; else: return False` can be simplified to `return cond`.
3. `getAlphaNumeric` could be a one-line list comprehension a la `return ''.join([ch for ch in text if ch.isalnum()])`
4. In `get_closest_extracted_string` the location of the Excel sheet must be configurable and therefore must not be hard-coded. There are multiple hard-coded Excel sheet locations in the file in addition to this one. ALL need to be fixed.
5. In `get_closest_extracted_string` we only consider the first value output from `cosine_similarity`. Is it possible for there to be more than one value? Numpy can handle division of vectors so a combination of that and np.max would find the largest cosine similarity among many values if necessary (use np.argmax if index is necessary).
6. In `extractTextFieldSpecific` it may be better to use a regex like `non.?diversified` (e.g. the text "non", then either a single character or nothing, then the text "diversified") to allow for many combinations such as "non-diversified" or "non diversified" in a single search.
7. In `extractTextFieldSpecific` we should write a private function that handles extracting arbitrary strings as in `AUDITOR` because it is likely this process will be repeated for other fields.
8. (* Reminder *) `assignValues` references a MongoDB connection string. This must be drawn from a consistent global configuration across all tasks. Also, `Task2_Demo` doesn't sound like the right database table. These table names should be drawn from a task-specific configuration.
9. (* _Major!_ *) In `assignValues` there is an if statement checking if `className != 'ClassA'`. This implies we will _ONLY_ retrieve values for Class A. Likewise, there is an if statement below `if field == 'NONDIVERSIFIED'` that implies we will _ONLY_ retrieve values for the specific field `NONDIVERSIFIED`. This seems wrong. Shouldn't we retrieve values for all valid Class and Field combinations? If the code only works for certain Field names, consider doing `if field in FIELDS` and define all valid fields in a set or list as a global constant.
10. In `assignValues` instead of using magic values for different kinds of value extraction (e.g. `if field in ['NONDIVERSIFIED' 'AUDITOR']`), there should be a globally applicable method of determining which fields need special handling. This is similar to what I suggested in item #7. This would make it easy to add new cases as well as reuse the same handling across multiple fields. If I were doing this from scratch, I would have used Python classes to define a consistent abstract interface and implement the interface across several different classes.
11. Lines 333-337 are just sloppy. They don't do anything at all. Reassigning the value of `item` only happens locally in the loop and it's immediately blown away by the next iteration of the loop. Put another way, `extractedTexts` is not being changed at all so these loops have no effect other than wasting CPU time. Ignoring that, why not just do both of these calls in a single loop?
12. (* Reminder *) Do not hardcode the results file path.
13. Instead of checking the `type` of `paragraphs_document[field]`, use `isinstance`. Only use `type` for raw types like `int` or `str` (and even then, `isinstance` should still work).
14. No need to write `f.close()` when in a `with open(...) as f` block. The `with` block automatically adds a `finally: f.close()` after the block.

# Task 4 GPT Text Extraction Code Comments
1. (* Reminder *) Correct all hardcoded file paths.
2. It might be a good idea to indicate that `make_para_prompt` should not be used anymore (e.g. mark as deprecated or something like that).
3. Same thing as item #10 above.
4. (* _Major!_ *) In `extract_text_from_para`: DO NOT COMMIT THE OPENAI API KEY. Use `openai.api_key_path` or similar to indicate a file that the API Key should be found at instead of giving it directly. Work with the other tasks to do this once at the start of the runner program.
5. The model should be configurable instead of locking to gpt-4. Maybe use a task-specific configuration file, sort of like for the MongoDB table names.
6. I remember that the `time.sleep(1.5)` is there to fix an issue on OpenAI's side. Instead of adding a comment that says what the line is doing, make the comment say _why_ we're doing it.
7. There's only one `generate_gpt_prompt#` so instead of calling it `generate_gpt_prompt1` maybe just `generate_gpt_prompt` (and in turn `training_prompt` instead of `training_prompt1`).
8. As a general comment, why are there any instances of "All Classes" positive _or_ negative samples being added to the list when we have a defined Class we're interested in? It seems like the "All Classes" examples would only be relevant when we are working with a Fund-level field. This is also in `bertValueAssignment`.

# Task 4 Other Files Code Comments
1. In `robertaClassification` would it make sense to allow using GPU if it is present? Or is this a case where inference is faster on the CPU (this is not uncommon)?
2. (* Reminder *) In `paragraphFiltering` correct the hardcoded file paths.
3. In `bertValueAssignment` you can just do `float('-inf')` instead of `-1 * float('inf')`.
4. `bertValueAssignment` has the same potential problem as item #5 from the Runner code comments.
5. In `bertValueAssignment` line 104 has an indentation error. It is indented 12 spaces instead of 8 spaces. Note that this fortunately won't change the functionality. Additionally, line 110 uses a same-line return on the `else` which is discouraged in Python.

# Task 4 Edge Cases and Error Cases
1. In `clean_text` it is possible we may want `re.sub("\s+", ...)` to use `"\s{2,}"` instead to prevent a case where we replace a single space with a single space (e.g. doing nothing).
2. In multiple places Task 4 will fail without a good error message if an Excel file is missing. It might be a good idea to wrap in `try: except:` and print a nice error message when the file is missing or is otherwise not formatted correctly (these should be the standard python IO exceptions). This is also true in `paragraphFiltering`.
3. If no texts are extracted in `get_closest_extracted_string` (so the list is empty) the final `return final_texts[-1][0]` will fail with an IndexError. It looks like there are some execution paths that ensure the input to this function (argument `extractedTexts`) cannot be empty, but perhaps not all of them.
4. In `extractRelevantText` if we don't get a `response` from GPT we will fail with a KeyError on `response['choices']` or an IndexError on `response['choices'][0]`. Should check to ensure we got a response from GPT and gracefully raise an exception or print an error message if not.
5. In `extractTextFieldSpecific` for both `NONDIVERSIFIED` as well as `INCOME_FREQUENCY` it looks like we will return `NOT_VALID` if the value is not present in the format we want. Is this ideal? (note: it might be okay -- obviously I lack some context into how this works)
6. In `assignValues` if either database call fails we don't print any messages to the console. Should check that we got a good result before proceeding with the task and print a message when we didn't.

# Task 4 Minor Comments
1. Global constants should be written in UPPERCASE_SNAKE_CASE to reflect that they are constants.
2. When using a global constant in a function you should define the constants in the first line of the function using `global CONSTANT_VALUE_1, CONSTANT_VALUE_2`.
3. You may know this already, but `if ls` is the same as `if len(ls) > 0`. Some people prefer to be more descriptive so this is fine.
4. In `get_closest_extracted_string` instead of `return final_texts[-1][0]`, consider using `reverse=True` on the `sort` call.
5. In `assignValues` the variable `df_columns` is unused.
6. In `robertaClassification` no need to set `result['status'] = False` since it started as `False`.