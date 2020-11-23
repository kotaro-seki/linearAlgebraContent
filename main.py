from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import numpy.linalg as LA

app = FastAPI()

@app.get("/")
def root():
    return {"path": "root"}

class Matrix(BaseModel):
    n: int
    matrix: List[List[int]]


@app.post("/determinant/")
def determinant(matrix: Matrix):
    determinant = LA.det(np.array(matrix.matrix))
    return {"n": matrix.n, "matrix": matrix.matrix, "determinant": determinant}
