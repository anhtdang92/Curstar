# Project Status & Roadmap

This document tracks the current status, planned features, known bugs, and future ideas for the STAR project.

## 🎯 Planned Features

- [ ] **Web Application Interface**
  - [x] Basic FastAPI backend structure
  - [x] Basic React/Next.js frontend with Material-UI
  - [x] Video upload and preview functionality
  - [x] Model selection interface
  - [x] Real-time progress tracking UI
  - [ ] Integrate STAR processing code into backend
  - [ ] Implement actual video processing pipeline
  - [ ] Add proper error handling and validation
  - [ ] Add user authentication system
  - [ ] Add batch processing capability
  - [ ] Add custom prompt input for models
  - [ ] Add processing history and results management
  - [ ] Add model configuration options
  - [ ] Add video format conversion options
  - [ ] Add processing queue management
  - [ ] Add email notifications for completed jobs

## 🐛 Known Bugs/Issues

- [ ] WebSocket connection may need reconnection logic for long-running processes
- [ ] Need to handle large file uploads properly
- [ ] Need to implement proper cleanup of temporary files
- [ ] Need to handle CUDA out-of-memory errors gracefully
- [ ] Need to implement proper error handling for failed processing jobs

## ✨ Future Ideas/Enhancements

- [ ] Add support for more video input formats
- [ ] Implement video preview thumbnails
- [ ] Add support for custom model configurations
- [ ] Add support for batch processing multiple videos
- [ ] Add support for video comparison (before/after)
- [ ] Add support for video quality metrics
- [ ] Add support for video metadata extraction
- [ ] Add support for video format conversion
- [ ] Add support for video compression
- [ ] Add support for video watermarking
- [ ] Add support for video trimming/cropping
- [ ] Add support for video effects
- [ ] Add support for video stabilization
- [ ] Add support for video denoising
- [ ] Add support for video color correction

## ✅ Completed Tasks

- [x] Fix `inference_sr.sh` execution in bash by directly calling venv python
- [x] Resolve `NameError: name 'argparse' is not defined` in `video_super_resolution/scripts/inference_sr.py`
- [x] Update documentation (README.md, .cursor.yaml) regarding `inference_sr.sh` fixes
- [x] Create this `PROJECT_STATUS.md` file
- [x] Set up basic FastAPI backend structure
- [x] Set up basic React/Next.js frontend with Material-UI
- [x] Implement video upload and preview functionality
- [x] Implement model selection interface
- [x] Implement real-time progress tracking UI
- [x] Added `start_backend.bat` script for Windows users to auto-activate venv and start the backend server with one command.
- [x] Added `start_frontend.bat` script for Windows users to easily start the Next.js frontend development server.
- [x] Added `start_servers.bat` script to start both backend and frontend servers with one command.
- [x] Upgraded frontend to Next.js 14.2.x and 15.x (latest as of May 2025)
- [x] Fixed hydration error: moved Material-UI theming to a client component (`theme-provider.tsx`) and made `layout.tsx` a server component
- [x] Added `git_push.bat` script for automated git add, commit, and push to origin main

## 🧪 Testing & Documentation

- [x] Added `run_test.ps1` for automated inference testing
- [ ] Write unit tests for backend
- [ ] Write unit tests for frontend
- [ ] Write integration tests
- [ ] Update API documentation
- [ ] Write user documentation
- [ ] Write developer documentation

## 🚀 Deployment
- [ ] Set up development environment
- [ ] Set up staging environment
- [ ] Set up production environment
- [ ] Set up CI/CD pipeline
- [ ] Set up monitoring and logging
- [ ] Set up backup and recovery

---
*Last Updated: 2025-05-12* 