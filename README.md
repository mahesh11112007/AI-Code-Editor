# AI-Code-Editor

An AI-powered code editor application with a FastAPI backend and Flutter mobile interface. This project demonstrates full-stack development with AI integration capabilities for intelligent code editing and analysis.

## 📋 Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [AI Integration](#ai-integration)
- [⚠️ Security Warning](#security-warning)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup (FastAPI)](#backend-setup-fastapi)
  - [Mobile Setup (Flutter)](#mobile-setup-flutter)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)

## 📁 Project Structure

```
AI-Code-Editor/
├── backend/                    # FastAPI backend server
│   ├── main.py                # Main FastAPI application
│   └── requirements.txt       # Python dependencies
├── mobile/                    # Flutter mobile application
│   ├── lib/                   # Flutter source code
│   │   └── main.dart         # Main Flutter application
│   ├── pubspec.yaml          # Flutter dependencies
│   └── README.md             # Mobile-specific documentation
└── README.md                  # This file
```

## ✨ Features

### Backend (FastAPI)

- **RESTful API Architecture**: Clean and scalable API design
- **CORS Support**: Cross-origin resource sharing enabled for mobile app integration
- **Health Check Endpoint**: Monitor backend service status
- **Fast Performance**: Built with FastAPI for high-performance async operations
- **Type Safety**: Pydantic models for request/response validation

### Mobile (Flutter)

- **Cross-Platform Support**: Runs on iOS and Android from a single codebase
- **Material Design UI**: Modern and intuitive user interface
- **HTTP Integration**: Seamless communication with backend API
- **State Management**: Provider pattern for efficient state handling
- **Responsive Design**: Optimized for various screen sizes

## 🤖 AI Integration

This project is designed with AI integration capabilities in mind:

- **Modular Architecture**: Easy to integrate AI/ML services
- **API-First Design**: Simple to connect with various AI providers
- **Scalable Backend**: FastAPI handles async AI operations efficiently

## ⚠️ Security Warning

**IMPORTANT: Environment Variables and API Keys**

**DO NOT** commit `.env` files or any files containing API keys, secrets, or credentials to this repository. The `.env` file has been removed from the repository and git history to protect exposed API keys.

### For Vercel Deployment:

When deploying to Vercel, **never** include environment variables in your code or repository. Instead, configure them securely through Vercel's dashboard:

1. Go to your Vercel project dashboard
2. Navigate to **Settings** → **Environment Variables**
3. Add your environment variables:
   - `OPENROUTER_API_KEY` - Your OpenRouter API key
   - Any other sensitive configuration values
4. Select the appropriate environments (Production, Preview, Development)
5. Click **Save**

### Best Practices:

- **Never** commit files containing secrets (`.env`, config files with keys, etc.)
- Always add `.env` to your `.gitignore` file
- Use Vercel's Environment Variables for all API keys and secrets
- Rotate any API keys that were previously exposed
- Use different API keys for development and production environments

### For Local Development:

Create a `.env` file in the `backend/` directory (this file is already in `.gitignore`):

```bash
OPENROUTER_API_KEY=your_api_key_here
```

**Remember**: This file should NEVER be committed to the repository.

## 🚀 Setup Instructions

### Backend Setup (FastAPI)

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables** (see Security Warning section above)

4. **Run the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```
   The server will start at http://localhost:8000

**Backend Dependencies**:
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [Uvicorn](https://www.uvicorn.org/) - ASGI server
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation

See [backend/requirements.txt](backend/requirements.txt) for complete dependency list.

### Mobile Setup (Flutter)

1. **Navigate to mobile directory**:
   ```bash
   cd mobile
   ```

2. **Install Flutter dependencies**:
   ```bash
   flutter pub get
   ```

3. **Update API endpoint** in `lib/main.dart`:
   ```dart
   final apiUrl = 'YOUR_BACKEND_URL';  // Update with your backend URL
   ```

4. **Run the mobile app**:
   ```bash
   flutter run
   ```
   Or use your IDE's run button (VS Code, Android Studio)

5. **Build for production**:
   ```bash
   # Android
   flutter build apk
   
   # iOS
   flutter build ios
   ```

**Mobile Dependencies**:
- [Flutter](https://flutter.dev/) - UI framework
- [HTTP](https://pub.dev/packages/http) - HTTP client for API calls
- [Provider](https://pub.dev/packages/provider) - State management

See [mobile/pubspec.yaml](mobile/pubspec.yaml) for complete dependency list and [mobile/README.md](mobile/README.md) for detailed mobile documentation.

## 📚 API Documentation

### Endpoints

**Root Endpoint**
```
GET /
Returns: Welcome message and API information
```

**Health Check**
```
GET /health
Returns: API status
```

For interactive API documentation, run the backend and visit http://localhost:8000/docs

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Quick Links

- [Backend Source Code](backend/main.py)
- [Backend Dependencies](backend/requirements.txt)
- [Mobile Source Code](mobile/lib/main.dart)
- [Mobile Dependencies](mobile/pubspec.yaml)
- [Mobile Documentation](mobile/README.md)

---

**Built with ❤️ using FastAPI and Flutter**
