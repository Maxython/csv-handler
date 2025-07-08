# csv-handler
A simple example of a parser/handler for `*.csv` files.

### Arguments:
- `--file` - path to `*.csv` file (required).
- `--where` - argument that allows to filter rows. Syntax: `header=value`, `header<value`, `header>value`.
- `--aggregate` - argument that allows to do mathematical subtraction according to rows. Syntax: `header=function`.
  Available mathematical functions:
  - `avg` - subtracts average values.
  - `min` - finds the minimum number.
  - `max` - finds the maximum number.

### Set up:
- Installation of required modules:
  ```bash
  pip install -r requirements.txt
  ```
- Enjoy:
  ```bash
  ./csv-handler.py --file products.csv
  ```

### Examples of use:
```bash
~ $ ./csv-handler.py --file test.csv
+------------------+---------+---------+----------+
| name             | brand   |   price |   rating |
|------------------+---------+---------+----------|
| iphone 15 pro    | apple   |     999 |      4.9 |
| galaxy s23 ultra | samsung |    1199 |      4.8 |
| redmi note 12    | xiaomi  |     199 |      4.6 |
| poco x5 pro      | xiaomi  |     299 |      4.4 |
+------------------+---------+---------+----------+
~ $ ./csv-handler.py --file test.csv --where "brand=samsung"
+------------------+---------+---------+----------+
| name             | brand   |   price |   rating |
|------------------+---------+---------+----------|
| galaxy s23 ultra | samsung |    1199 |      4.8 |
+------------------+---------+---------+----------+
~ $ ./csv-handler.py --file test.csv --aggregate "rating=avg"
+-------+
|   avg |
|-------|
|  4.67 |
+-------+
~ $ ./csv-handler.py --file products.csv --where "brand=apple" --aggregate "price=avg"
+-------+
|   avg |
|-------|
| 706.5 |
+-------+
```
