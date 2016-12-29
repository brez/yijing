# Consulting the Oracle

Python library for consulting the Yijing / I Ching. 

## Usage

There are two primary methods, `predict` does the traditional method for creating the hexagram lines. You can then `lookup` the hexagram and complete the reading.
 
    from yijing import iching
    
    seed = "?" # something random or meaningful but unique
    prediction = iching.predict(seed)
    print(iching.lookup(prediction)

## Quote

    "Countless words count less than the silent balance between yin and yang"
      - Lao Tzu, Tao Te Ching


### Notes

* Python 3 only
* Doesn't include the interpretations
