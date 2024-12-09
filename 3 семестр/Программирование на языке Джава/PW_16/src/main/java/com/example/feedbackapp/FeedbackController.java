package com.example.feedbackapp;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class FeedbackController {

	@GetMapping("/home")
	public String showForm() {
		return "home"; // Имя HTML-файла, который должен быть в папке templates
	}

	@GetMapping("/")
	public String redirectToHome() {
		return "redirect:/home"; // Перенаправление на /home
	}

	@PostMapping("/home")
	public String handleForm(@RequestParam String name,
							 @RequestParam String email,
							 @RequestParam String message,
							 Model model) {
		// Здесь можно сохранить сообщение в базу (пока просто показываем ответ)
		model.addAttribute("feedback", "Спасибо, " + name + "! Ваше сообщение отправлено.");
		return "home"; // Вернём ту же страницу с подтверждением
	}

	@Controller
	public class LoginController {

		@GetMapping("/login")
		public String login() {
			return "login"; // Возвращает файл login.html
		}
	}
}
