import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import OperationalError

# Параметры подключения (замените на свои!)
DB_CONFIG = {
    "host": "localhost",
    "database": "myapp_db",
    "user": "postgres",
    "password": "1234",
    "port": "5432"
}

def get_connection():
    """Создаёт и возвращает новое подключение к БД."""
    return psycopg2.connect(**DB_CONFIG)

# 1. CREATE — добавление записи
def create_product(name: str, price: float, in_stock: bool = True):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO products (name, price, in_stock) VALUES (%s, %s, %s);",
                    (name, price, in_stock)
                )
                conn.commit()
                print(f"✅ Продукт '{name}' добавлен.")
    except Exception as e:
        print(f"❌ Ошибка при добавлении: {e}")

# 2. READ — получение всех записей
def get_all_products():
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM products;")
                records = cur.fetchall()
                return [dict(record) for record in records]  # Преобразуем в обычные словари
    except Exception as e:
        print(f"❌ Ошибка при чтении: {e}")
        return []

# 3. UPDATE — обновление записи
def update_product(product_id: int, name: str = None, price: float = None, in_stock: bool = None):
    fields = []
    values = []
    
    if name is not None:
        fields.append("name = %s")
        values.append(name)
    if price is not None:
        fields.append("price = %s")
        values.append(price)
    if in_stock is not None:
        fields.append("in_stock = %s")
        values.append(in_stock)
    
    if not fields:
        print("⚠️ Нечего обновлять.")
        return

    values.append(product_id)  # для WHERE id = %s

    query = f"UPDATE products SET {', '.join(fields)} WHERE id = %s;"
    
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)
                conn.commit()
                print(f"✅ Продукт с id={product_id} обновлён.")
    except Exception as e:
        print(f"❌ Ошибка при обновлении: {e}")

# 4. DELETE — удаление записи
def delete_product(product_id: int):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM products WHERE id = %s;", (product_id,))
                conn.commit()
                print(f"🗑️ Продукт с id={product_id} удалён.")
    except Exception as e:
        print(f"❌ Ошибка при удалении: {e}")

# ----------------------------
# Демонстрация работы
# ----------------------------
if __name__ == "__main__":
    # Создаём два продукта
    create_product("Наушники", 2500.00, True)
    create_product("Зарядка", 800.50, False)

    # Читаем все
    print("\n📋 Все продукты:")
    for p in get_all_products():
        print(p)

    # Обновляем один
    update_product(1, price=2300.00, in_stock=False)

    # Удаляем другой
    delete_product(2)

    # Финальный вывод
    print("\n🔄 После изменений:")
    for p in get_all_products():
        print(p)