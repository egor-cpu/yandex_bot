import yadisk

y = yadisk.YaDisk(token="y0_AgAAAABWsXjrAAySrgAAAAETpT3RAAB4d_H72nRPeo_nVzmz1CDWFma67w")
# или
# y = yadisk.YaDisk("<id-приложения>", "<secret-приложения>", "<токен>")

# Проверяет, валиден ли токен
print(y.check_token())

# Получает общую информацию о диске
print(y.get_disk_info())

# Выводит содержимое "/some/path"
print(list(y.listdir("/some/path")))

# Загружает "file_to_upload.txt" в "/destination.txt"
y.upload("file_to_upload.txt", "/destination.txt")

# То же самое
with open("file_to_upload.txt", "rb") as f:
    y.upload(f, "/destination.txt")

# Скачивает "/some-file-to-download.txt" в "downloaded.txt"
y.download("/some-file-to-download.txt", "downloaded.txt")

# Безвозвратно удаляет "/file-to-remove"
y.remove("/file-to-remove", permanently=True)

# Создаёт новую папку "/test-dir"
print(y.mkdir("/test-dir"))