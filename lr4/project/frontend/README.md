# Проект: Интернет-каталог товаров

Кратко: проект состоит из трёх частей — PostgreSQL (Docker), backend (Node.js + Express) и frontend (React). Ниже шаги для запуска локально в параллельных терминалах/окнах.

Требования:
- Docker / Docker Desktop
- Node.js (16+)
- npm

Порты по умолчанию:
- PostgreSQL: 5432
- Adminer: 8080 (опционально)
- Backend (Express): 5000
- Frontend (React CRA): 3000

1) Перейдите в папку проекта

```powershell
cd REACT01/2/project
```

2) Поднимите базу данных (в отдельном терминале)

Используйте `docker compose` (или `docker-compose` если у вас старая версия):

```powershell
docker compose up -d
# или
docker-compose up -d
```

Проверка запущенных контейнеров:

```powershell
docker ps
```

Если хотите посмотреть логи и убедиться, что `init.sql` выполнился:

```powershell
docker compose logs -f postgres
```

Подключиться к БД внутри контейнера (psql):

```powershell
docker exec -it my_postgres psql -U user -d shopdb
# затем в psql можно выполнить: \dt   и  SELECT COUNT(*) FROM products;
```

3) Запустите backend (в новом терминале)

```powershell
cd REACT01/2/project/backend
npm install
# настройте .env при необходимости (если подключаетесь к контейнеру по-другому)
npm start
# или для разработки
npm run dev
```

Примечание: если backend запускается на хосте (не в контейнере), то в `backend/.env` оставьте `DB_HOST=localhost` (порт 5432 проброшен). Если вы контейнеризируете backend, используйте название сервиса `postgres` как хост.

4) Запустите frontend (в новом терминале)

```powershell
cd REACT01/2/project/frontend
npm install
npm start
```

Откройте в браузере: http://localhost:3000

5) Тестирование и отладка
- Переключитесь по категориям в сайдбаре — приложение вызывает `GET /api/products?category=...&page=...`.
- Если не видите данных, проверьте логи backend и убедитесь, что подключение к БД успешно (в логах будет "Подключено к PostgreSQL" или сообщение об ошибке).

6) Остановка

```powershell
docker compose down
# или
docker-compose down
```

Полезные советы:
- Убедитесь, что Docker Desktop запущен и у него достаточно ресурсов.
- Если порт 3000 занят, React предложит другой порт — применяйте его в браузере.
- Для быстрого просмотра БД можно открыть Adminer: http://localhost:8080 (если сервис включён).

Если хотите, могу автоматически открыть терминалы и запустить команды (требует управления вашей средой) или собрать zip архива проекта для отправки/сдачи.

---

Автоматический запуск (Windows PowerShell)

В корне проекта добавлены helper-скрипты для удобного запуска в Windows:

- `setup.ps1` — один раз устанавливает зависимости для backend и frontend.
- `start-all.ps1` — поднимает Docker и открывает два окна PowerShell: backend и frontend (они запускают `npm start`).
- `stop-all.ps1` — останавливает и удаляет контейнеры Docker.

Запуск из PowerShell (если требуется разрешить выполнение скриптов на время):

```powershell
# один раз подготовить проект
.\setup.ps1

# запустить всё (откроет окна для backend и frontend)
.\start-all.ps1

# после работы остановить контейнеры
.\stop-all.ps1
```

Примечание:
- Если PowerShell блокирует запуск локальных скриптов, выполните в сессии: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.
- Скрипты открывают новые окна терминала через `Start-Process` — вы увидите отдельные окна для backend и frontend, где будут логи запуска.

Если хотите, добавлю эти скрипты прямо сейчас (они автоматически созданы по вашему запросу). 
