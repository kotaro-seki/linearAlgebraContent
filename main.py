from typing import List

import numpy as np
import numpy.linalg as LA
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def root():
    return {'path': 'root'}


class Matrix(BaseModel):
    n: int
    matrix: List[List[int]]


@app.post('/determinant/')
def determinant(matrix: Matrix):
    if not is_n_dimension_matrix(matrix):
        return make_error_response('渡された行列がN次の正方行列ではありませんでした。')
    determinant = LA.det(np.array(matrix.matrix))
    return {'n': matrix.n, 'matrix': matrix.matrix, 'determinant': determinant}


def is_n_dimension_matrix(matrix: Matrix) -> bool:
    if len(matrix.matrix) != matrix.n:
        return False
    for row in matrix.matrix:
        if len(row) != matrix.n:
            return False
    return True


def make_error_response(error_message: str) -> dict:
    return {
        'status': 'error',
        'error_message': error_message
    }
