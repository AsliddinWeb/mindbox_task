from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# Инициализация SparkSession
spark = SparkSession.builder \
    .appName("ProductCategoryPairs") \
    .getOrCreate()

# Пример датафреймов
products_df = spark.createDataFrame([
    (1, "Product A"),
    (2, "Product B"),
    (3, "Product C"),
    (4, "Product D")
], ["product_id", "product_name"])

categories_df = spark.createDataFrame([
    (1, "Category 1"),
    (2, "Category 2"),
    (3, "Category 3")
], ["category_id", "category_name"])

product_category_df = spark.createDataFrame([
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 3)
], ["product_id", "category_id"])


def get_product_category_pairs(products_df, categories_df, product_category_df):
    # Объединение продуктов и связей
    product_category_joined_df = products_df.join(product_category_df, "product_id", "left_outer")

    # Объединение с категориями для получения имен категорий
    product_category_pairs_df = product_category_joined_df.join(categories_df, "category_id", "left_outer") \
        .select("product_name", "category_name")

    # Продукты без категорий
    products_without_categories_df = product_category_pairs_df.filter(col("category_name").isNull()) \
        .select("product_name") \
        .withColumn("category_name", lit(None))  # Добавление пустой колонки category_name

    # Комбинирование всех пар
    result_df = product_category_pairs_df.union(products_without_categories_df)

    return result_df


# Вызов функции
result_df = get_product_category_pairs(products_df, categories_df, product_category_df)
result_df.show()
