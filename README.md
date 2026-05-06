# SIT333 9.1P - TDD and CI

## Project Overview

This project is a simple OnTrack task submission checker. It checks if a student has entered student ID, task ID and uploaded a PDF file.

## Function

The function name is:

submit_task(student_id, task_id, file_name)

## Rules

- Student ID must not be empty.
- Task ID must not be empty.
- File name must not be empty.
- File must be a PDF file.
- If all details are correct, the task is submitted successfully.

## Testing

This project uses pytest for unit testing.

To run tests:

python -m pytest

## CI

GitHub Actions is used for Continuous Integration. It automatically runs all tests when code is pushed to GitHub.
