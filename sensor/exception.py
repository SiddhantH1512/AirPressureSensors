import sys
import os

def error_message_detail(error, error_detail: sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = f"Error occure in script name {filename}, Line number {line_no} and error message is {str(error)}"

    return error_message


class SensorException(Exception):
    def __init__(self, error, error_message: sys):
        super().__init__(error)
        self.error = error
        self.error_message = error_message_detail(error, error_message)

    def __str__(self):
        return self.error_message