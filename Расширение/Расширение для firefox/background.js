// Храним уже обнаруженные куки
const knownCookies = new Set();

// Функция для проверки, является ли кука подозрительной
function isSuspiciousCookie(cookie) {
  // Проверяем, что куки не имеют secure и httpOnly
  if (cookie.secure || cookie.httpOnly) {
    return false;
  }

  // Проверяем длину значения куки
  if (cookie.value.length > 100) {
    return true; // Слишком длинное значение
  }

  // Проверяем имя куки на наличие подозрительных подстрок
  const suspiciousNames = ['sessionid', 'token', 'auth', 'login'];
  if (suspiciousNames.some(name => cookie.name.toLowerCase().includes(name))) {
    return true; // Подозрительное имя
  }

  // Проверяем домен куки (можно добавить свои подозрительные домены)
  const suspiciousDomains = ['malicious.com', 'fake.com'];
  if (suspiciousDomains.includes(cookie.domain)) {
    return true; // Подозрительный домен
  }

  return false; // Кука не подозрительная
}

// Функция для отправки подозрительных куков на сервер
function sendSuspiciousCookies(cookies) {
  console.log("Sending suspicious cookies:", cookies); // Отладочное сообщение
  fetch('http://localhost:5000/suspicious_cookies', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(cookies),
  })
  .then(response => {
    if (response.ok) {
      console.log('Suspicious cookies sent to server.');
    } else {
      console.error('Error sending suspicious cookies:', response.statusText);
    }
  })
  .catch(error => console.error('Error:', error));
}

// Функция для проверки наличия подозрительных куков
function checkForSuspiciousCookies() {
  console.log("Checking for suspicious cookies..."); // Отладочное сообщение
  browser.cookies.getAll({}, (cookies) => {
    console.log("Cookies retrieved:", cookies); // Отладочное сообщение
    let suspiciousCookies = [];

    cookies.forEach(cookie => {
      // Проверяем, является ли кука новой
      if (!knownCookies.has(cookie.name) && isSuspiciousCookie(cookie)) {
        console.log("New suspicious cookie detected:", cookie);
        suspiciousCookies.push(cookie);
        // Добавляем куку в известные
        knownCookies.add(cookie.name);
      }
    });

    // Если найдены подозрительные куки, отправляем их на сервер
    if (suspiciousCookies.length > 0) {
      console.log("Suspicious cookies found:", suspiciousCookies);
      sendSuspiciousCookies(suspiciousCookies);
    } else {
      console.log("No new suspicious cookies found."); // Отладочное сообщение
    }
  });
}

// Устанавливаем интервал для периодической проверки куков
setInterval(checkForSuspiciousCookies, 5000); // Проверка каждые 5 секунд

// Также можно вызвать функцию сразу при запуске расширения
checkForSuspiciousCookies();
