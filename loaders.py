from datetime import datetime
from tqdm import tqdm
from datasets import load_dataset
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from items import Item


CHUNK_SIZE = 1000
MIN_PRICE = 0.5
MAX_PRICE = 999.49


class ItemLoader:


    def __init__(self, name):
        self.name = name
        self.dataset = None


    def from_datapoint(self, datapoint):


        try:
            price_str = datapoint['price']
            if price_str:
                price = float(price_str)
                if MIN_PRICE <= price <= MAX_PRICE:
                    item = Item(datapoint,price)
                    return item if item.include else None
        except ValueError:
            return None
        
    def from_chunk(self, chunk):
        
        batch = []
        for datapoint in chunk:
            result = self.from_datapoint()
            if result:
                batch.append(result)
        return batch
    
    def chunk_generator(self):
        
        size = len(self.dataset)
        for i in range(0,size, CHUNK_SIZE):
            yield self.dataset.select(range(i,min(i+CHUNK_SIZE, size)))
    
    # def load_in_parallel(self, workers):


    #     result = []