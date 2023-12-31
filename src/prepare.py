from dvc import api
import pandas as pd
from io import StringIO
import sys
import logging 

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s", 
    level=logging.INFO, 
    datefmt="%H:%M:%S",
    stream=sys.stderr
)

logger = logging.getLogger(__name__)
logging.info("Fetching data...")

movie_data_path = api.read("notebooks/dataset/movies.csv", remote="dataset-track")
financial_data_path = api.read("notebooks/dataset/financials.csv", remote="dataset-track")
opening_data_path = api.read("notebooks/dataset/opening_gross.csv", remote="dataset-track")

fin_data = pd.read_csv(StringIO(financial_data_path))
movie_data = pd.read_csv(StringIO(movie_data_path))
opening_data = pd.read_csv(StringIO(opening_data_path))

breakpoint()