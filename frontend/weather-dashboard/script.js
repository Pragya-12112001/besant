
const searchForm = document.getElementById("searchForm");
const cityInput = document.getElementById("cityInput");
const searchBtn = document.getElementById("searchBtn");
const message = document.getElementById("message");
const weatherContent = document.getElementById("weatherContent");

const weatherCodes = {
    0: { description: "Clear sky", icon: "☀️" },
    1: { description: "Mainly clear", icon: "🌤️" },
    2: { description: "Partly cloudy", icon: "⛅" },
    3: { description: "Overcast", icon: "☁️" },
    45: { description: "Foggy", icon: "🌫️" },
    48: { description: "Depositing rime fog", icon: "🌫️" },
    51: { description: "Light drizzle", icon: "🌦️" },
    53: { description: "Moderate drizzle", icon: "🌦️" },
    55: { description: "Dense drizzle", icon: "🌧️" },
    61: { description: "Slight rain", icon: "🌦️" },
    63: { description: "Moderate rain", icon: "🌧️" },
    65: { description: "Heavy rain", icon: "🌧️" },
    71: { description: "Slight snowfall", icon: "🌨️" },
    73: { description: "Moderate snowfall", icon: "❄️" },
    75: { description: "Heavy snowfall", icon: "❄️" },
    80: { description: "Slight rain showers", icon: "🌦️" },
    81: { description: "Moderate rain showers", icon: "🌧️" },
    82: { description: "Violent rain showers", icon: "⛈️" },
    95: { description: "Thunderstorm", icon: "⛈️" },
    96: { description: "Thunderstorm with hail", icon: "⛈️" },
    99: { description: "Thunderstorm with heavy hail", icon: "⛈️" }
};

// Handle search form submission
searchForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const city = cityInput.value.trim();

    if (!city) {
        showMessage("Please enter a city name.");
        return;
    }

    await searchWeather(city);
});

// Main function
async function searchWeather(city) {
    try {
        setLoading(true);
        showMessage("");

        // Step 1: Get city coordinates
        const location = await getCityCoordinates(city);

        if (!location) {
            throw new Error("City not found. Please try another city.");
        }

        // Step 2: Fetch weather data
        const weatherData = await getWeatherData(
            location.latitude,
            location.longitude
        );

        // Step 3: Display weather information
        displayCurrentWeather(location, weatherData);
        displayHourlyForecast(weatherData);
        displayDailyForecast(weatherData);

        weatherContent.hidden = false;

    } catch (error) {
        weatherContent.hidden = true;
        showMessage(error.message);
    } finally {
        setLoading(false);
    }
}

// Fetch city coordinates using Geocoding API
async function getCityCoordinates(city) {
    const url = new URL(
        "https://geocoding-api.open-meteo.com/v1/search"
    );

    url.search = new URLSearchParams({
        name: city,
        count: 1,
        language: "en",
        format: "json"
    });

    const response = await fetch(url);

    if (!response.ok) {
        throw new Error("Unable to find location.");
    }

    const data = await response.json();

    return data.results?.[0] || null;
}

// Fetch weather using latitude and longitude
async function getWeatherData(latitude, longitude) {
    const url = new URL(
        "https://api.open-meteo.com/v1/forecast"
    );

    url.search = new URLSearchParams({
        latitude,
        longitude,
        current: [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "precipitation",
            "weather_code",
            "cloud_cover",
            "wind_speed_10m",
            "is_day"
        ].join(","),
        hourly: [
            "temperature_2m",
            "weather_code",
            "precipitation_probability"
        ].join(","),
        daily: [
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_probability_max"
        ].join(","),
        timezone: "auto",
        forecast_days: 7
    });

    const response = await fetch(url);

    if (!response.ok) {
        throw new Error("Unable to fetch weather data.");
    }

    return await response.json();
}

// Display current weather
function displayCurrentWeather(location, data) {
    const current = data.current;
    const condition = getWeatherInfo(current.weather_code);

    document.getElementById("cityName").textContent =
        `${location.name}, ${location.country}`;

    document.getElementById("currentDate").textContent =
        formatDate(current.time);

    document.getElementById("weatherIcon").textContent =
        condition.icon;

    document.getElementById("temperature").textContent =
        `${Math.round(current.temperature_2m)}°`;

    document.getElementById("weatherDescription").textContent =
        condition.description;

    document.getElementById("feelsLike").textContent =
        `Feels like ${Math.round(current.apparent_temperature)}°C`;

    document.getElementById("humidity").textContent =
        `${current.relative_humidity_2m}%`;

    document.getElementById("windSpeed").textContent =
        `${current.wind_speed_10m} km/h`;

    document.getElementById("precipitation").textContent =
        `${current.precipitation} mm`;

    document.getElementById("cloudCover").textContent =
        `${current.cloud_cover}%`;
}

// Display hourly forecast
function displayHourlyForecast(data) {
    const hourlyContainer =
        document.getElementById("hourlyForecast");

    hourlyContainer.replaceChildren();

    const hourly = data.hourly;
    const currentTime = data.current.time;

    // Find the current hour in the hourly forecast
    let startIndex = hourly.time.findIndex(
        time => time >= currentTime
    );

    if (startIndex === -1) startIndex = 0;

    // Display the next 8 hours
    const forecast = hourly.time.slice(
        startIndex,
        startIndex + 8
    );

    forecast.forEach((time, index) => {
        const actualIndex = startIndex + index;
        const condition = getWeatherInfo(
            hourly.weather_code[actualIndex]
        );

        const card = document.createElement("div");
        card.className = "hour-card";

        const timeElement = document.createElement("p");
        timeElement.textContent = formatHour(time);

        const iconElement = document.createElement("div");
        iconElement.className = "hour-icon";
        iconElement.textContent = condition.icon;

        const temperatureElement = document.createElement("h3");
        temperatureElement.textContent =
            `${Math.round(hourly.temperature_2m[actualIndex])}°`;

        card.append(timeElement, iconElement, temperatureElement);
        hourlyContainer.appendChild(card);
    });
}

// Display 7-day forecast
function displayDailyForecast(data) {
    const dailyContainer =
        document.getElementById("dailyForecast");

    dailyContainer.replaceChildren();

    const daily = data.daily;

    daily.time.forEach((date, index) => {
        const condition = getWeatherInfo(
            daily.weather_code[index]
        );

        const card = document.createElement("div");
        card.className = "day-card";

        const dayName = document.createElement("span");
        dayName.className = "day-name";
        dayName.textContent = formatDay(date);

        const icon = document.createElement("span");
        icon.className = "day-icon";
        icon.textContent = condition.icon;

        const description = document.createElement("span");
        description.className = "day-description";
        description.textContent = condition.description;

        const temperature = document.createElement("span");
        temperature.className = "day-temperature";
        temperature.textContent =
            `${Math.round(daily.temperature_2m_max[index])}° / ` +
            `${Math.round(daily.temperature_2m_min[index])}°`;

        card.append(dayName, icon, description, temperature);

        dailyContainer.appendChild(card);
    });
}

// Get weather description and icon
function getWeatherInfo(code) {
    return weatherCodes[code] || {
        description: "Unknown weather",
        icon: "🌡️"
    };
}

// Format date
function formatDate(date) {
    return new Date(date).toLocaleDateString("en-US", {
        weekday: "long",
        day: "numeric",
        month: "long"
    });
}

// Format hour
function formatHour(time) {
    return new Date(time).toLocaleTimeString("en-US", {
        hour: "numeric",
        hour12: true
    });
}

// Format day
function formatDay(date) {
    return new Date(`${date}T12:00:00`).toLocaleDateString(
        "en-US",
        { weekday: "short" }
    );
}

// Loading state
function setLoading(isLoading) {
    searchBtn.disabled = isLoading;
    searchBtn.textContent = isLoading ? "Searching..." : "Search";
}

// Display errors
function showMessage(text) {
    message.textContent = text;
}
