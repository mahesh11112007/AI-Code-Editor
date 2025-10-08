# AI-Code-Editor

An AI-powered code editor application with a FastAPI backend and Flutter mobile interface. This project demonstrates full-stack development with AI integration capabilities for intelligent code editing and analysis.

## 📋 Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [AI Integration](#ai-integration)
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
- **API-First Design**: Backend ready for AI model endpoints
- **Extensible Structure**: Add AI features like:
  - Code completion and suggestions
  - Syntax error detection
  - Code quality analysis
  - Smart refactoring recommendations
  - Natural language to code conversion

**Note**: AI models can be integrated through the [FastAPI backend](backend/main.py) by adding new endpoints and connecting to AI services (OpenAI, Hugging Face, etc.)

## 🚀 Setup Instructions

### Backend Setup (FastAPI)

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**:
   - API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - Alternative API docs: http://localhost:8000/redoc

**Backend Dependencies**:
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework for building APIs
- [Uvicorn](https://www.uvicorn.org/) - ASGI server
- [Pydantic](https://docs.pydantic.dev/) - Data validation
- [Python-Multipart](https://andrew-d.github.io/python-multipart/) - File upload support

See [backend/requirements.txt](backend/requirements.txt) for version details.

### Mobile Setup (Flutter)

1. **Prerequisites**:
   - Install [Flutter SDK](https://flutter.dev/docs/get-started/install)
   - Install [Android Studio](https://developer.android.com/studio) or [Xcode](https://developer.apple.com/xcode/) (for iOS)

2. **Navigate to the mobile directory**:
   ```bash
   cd mobile
   ```

3. **Install Flutter dependencies**:
   ```bash
   flutter pub get
   ```

4. **Run the app**:
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
