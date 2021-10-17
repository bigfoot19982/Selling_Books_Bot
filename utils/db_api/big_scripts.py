# preparing scripts for postgresql.py file

create_tab_books = """
        CREATE TABLE IF NOT EXISTS books (
        book_id INT,
        book_name VARCHAR(200) NOT NULL,
        author VARCHAR(100) NOT NULL,
        units_in_stock INT,
        PRIMARY KEY(book_id));
        
        INSERT INTO books  
        VALUES 
        (1, 'Учебник Кузьмина', 'Сергей Андреевич Кузьмин', 1),
        (2, 'Учебник Яковенко', 'Э.В. Яковенко', 1),
        (3, 'Учебник Яковенко по политпереводу', 'Э.В. Яковенко', 1),
        (4, 'Россия на рубеже XV-XVI столетий', 'А.А. Зимин', 1),
        (5, 'История российская IX-XVII веков', 'Р.Г. Скрынников', 1),
        (6, 'Иван Грозный', 'Р.Г. Скрынников', 1),
        (7, 'Искра жизни', 'Ф. Эшкрофт', 1),
        (8, 'Расширенный фенотип', 'Р. Докинз', 1),
        (9, 'Происхождение жизни', 'М. Никитин', 1),
        (10, 'Эгоистичный ген', 'Р. Докинз', 1),
        (11, 'Мозг и душа', 'Крис Фрит', 1)
        """

create_tab_orders = """
        CREATE TABLE IF NOT EXISTS orders (
        order_id serial NOT NULL,
        book_id INT NOT NULL,
        buyer_name VARCHAR(255) NOT NULL,
        phone text NOT NULL,
        shipping_address text NOT NULL,
        total_amount bigint NOT NULL,
        shipping_option VARCHAR NOT NULL,
        order_date timestamp NOT NULL,
        done Bool DEFAULT False,
        PRIMARY KEY(order_id))
        """

order_data = """
        SELECT buyer_name, book_name, order_id
        FROM orders
        JOIN books USING(book_id)
        WHERE order_id = $1
        """
get_ship_address = "SELECT shipping_address FROM orders WHERE order_id = $1"

how_much = "SELECT COUNT (*) FROM books WHERE book_id = $1 AND units_in_stock > 0"

add_ord = "INSERT INTO orders (book_id, buyer_name, phone, shipping_address, total_amount, shipping_option, order_date, done) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)"

count_units_in_stock = "SELECT COUNT (units_in_stock) FROM books WHERE book_id = $1"

update_units_in_stock = "UPDATE books SET units_in_stock = $1 WHERE book_id = $2"

last_order = "SELECT MAX(order_id) FROM orders"

ask_ship_opt = "SELECT shipping_option FROM orders WHERE order_id = $1"
