# Python Microservice Template

A production-ready Python template for building scalable microservices. This template is designed to be used as a starting point for various services including Middleware, Indexer, Upsertion, and Retriever components.

## 🏗 Project Structure

```
├── app/                    # Application source code
│   ├── api/               # API routes and endpoints
│   ├── core/              # Core functionality and config
│   ├── models/            # Data models and schemas
│   ├── services/          # Business logic
│   └── utils/             # Utility functions
├── tests/                 # Test suite
├── scripts/               # Utility scripts
├── docs/                  # Documentation
├── .env.example          # Example environment variables
├── .envrc               # Direnv configuration
├── .gitignore           # Git ignore rules
├── Dockerfile           # Container definition
├── Makefile            # Build automation
├── pyproject.toml      # Project metadata and dependencies
└── README.md           # Project documentation
```

## 🎯 Why This Structure?

1. **Modularity**: The structure separates concerns into distinct directories, making it easy to locate and maintain code.
2. **Scalability**: Designed to handle growth in both codebase and team size.
3. **Testing**: Dedicated test directory with the same structure as the source code.
4. **Configuration**: Environment-based configuration with support for local development.
5. **Documentation**: Comprehensive documentation structure for maintaining project knowledge.

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Docker
- Make
- uv (Install with: `curl -LsSf https://astral.sh/uv/install.sh | sh`)

### Local Development Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <project-name>
   ```

2. Install dependencies using uv:

   ```bash
   make install
   ```

   This will:

   - Create a virtual environment using uv
   - Install project dependencies
   - Set up pre-commit hooks

3. Copy environment variables:

   ```bash
   cp .env.example .env
   ```

4. Run the development server:
   ```bash
   make run
   ```

### Using Docker

1. Build the container:

   ```bash
   make docker-build
   ```

2. Run the container:
   ```bash
   make docker-run
   ```

## 🛠 Development Commands

- `make install`: Install dependencies using uv
- `make test`: Run tests
- `make lint`: Run linting checks
- `make format`: Format code
- `make clean`: Clean build artifacts
- `make docker-build`: Build Docker image
- `make docker-run`: Run Docker container

## 📚 Using This Template

1. **Create New Project**:

   ```bash
   git clone <template-repo-url> new-project
   cd new-project
   rm -rf .git
   git init
   ```

2. **Update Configuration**:

   - Modify `pyproject.toml` with your project details
   - Update environment variables in `.env.example`
   - Adjust Dockerfile if needed

3. **Add Your Code**:

   - Place API routes in `app/api/`
   - Add business logic in `app/services/`
   - Define models in `app/models/`
   - Add tests in `tests/`

4. **Documentation**:
   - Update this README with project-specific information
   - Add API documentation in `docs/`
   - Document architectural decisions in `docs/adr/`

## 🤝 Contributing

1. Create a new branch
2. Make your changes
3. Run tests and linting
4. Submit a pull request

## 📝 License

[MIT License](LICENSE)
