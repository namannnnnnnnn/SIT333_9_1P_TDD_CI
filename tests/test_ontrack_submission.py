from ontrack_submission import submit_task


def test_valid_pdf_submission():
    result = submit_task("225176816", "SIT333-9.1P", "report.pdf")
    assert result == "Task submitted successfully"


def test_empty_student_id():
    result = submit_task("", "SIT333-9.1P", "report.pdf")
    assert result == "Student ID is required"


def test_empty_task_id():
    result = submit_task("225176816", "", "report.pdf")
    assert result == "Task ID is required"


def test_non_pdf_file():
    result = submit_task("225176816", "SIT333-9.1P", "report.docx")
    assert result == "Only PDF files are allowed"


def test_empty_file_name():
    result = submit_task("225176816", "SIT333-9.1P", "")
    assert result == "File name is required"
