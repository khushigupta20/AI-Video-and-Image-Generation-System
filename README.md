# **AI Video and Image Generation System**

This repository contains the **AI Video and Image Generation System Assignment**, which leverages AI tools to create motivational videos and images based on user-provided text prompts. While the project is currently incomplete, core functionality has been implemented to lay the foundation for future development.

---

## **Features Implemented**

### 1. **Text-to-Image Generation**  
- **Tool Used**: OpenAI’s DALL·E  
- **Implemented Features**:  
  - Accepts a user-provided text prompt.
  - Generates images based on the text.
  - Saves generated images in the directory structure: `generated_content/<user_id>/`.

### 2. **Storage Management**  
- Generated images are stored in a structured directory for easy access.

### 3. **Web Interface (Partial)**  
- **Framework Used**: Flask  
- **Implemented Features**:  
  - Basic routing and setup.  
  - Placeholder for user login and content display.

---

## **Features Yet to Be Implemented**
1. **Text-to-Video Generation**: Integration of tools like RunwayML or Pictory.ai for generating videos.  
2. **Database Management**: A database to store user data, prompts, and generation status.  
3. **Notifications**: Email or system notifications to inform users when their content is ready.  
4. **Web Interface Enhancements**: Full gallery and grid views for generated videos and images.  
5. **Logging**: Track user login attempts and content views.

---

## **Setup Instructions**

### 1. Clone the Repository  
```bash
git clone https://github.com/khushigupta20/AI-Video-and-Image-Generation-System.git
cd AI-Video-and-Image-Generation-System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the System
Currently, only partial functionality is implemented. To test text-to-image generation:  
```bash
python main.py
```

### 4. API Configuration
Add your OpenAI API key in `main.py` to enable image generation functionality.

---

## **Challenges and Limitations**
- The project is **incomplete** due to time constraints, as I was occupied with my **7th-semester end examinations**.
- I could only dedicate **one day** to this assignment but have implemented the foundational features to ensure future extensibility.

---

## **Future Scope**
1. Complete video generation functionality using RunwayML or similar tools.  
2. Implement a robust database for managing user and content information.  
3. Build a fully functional web interface for content display and user interaction.  
4. Add notification and logging features for improved user experience.  
5. Optimize the system for scalability and efficiency.

# Vedio Explanation
Link: https://drive.google.com/file/d/1uHlq_jwq_MvrfHMQgwXSqrJa3QKQtWBc/view?usp=sharing
