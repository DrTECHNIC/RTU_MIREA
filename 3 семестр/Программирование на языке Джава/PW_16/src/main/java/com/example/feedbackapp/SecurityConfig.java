package com.example.feedbackapp;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public UserDetailsService userDetailsService() {
        return new InMemoryUserDetailsManager(
                User.withDefaultPasswordEncoder()
                        .username("user")
                        .password("password")
                        .roles("USER")
                        .build()
        );
    }

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
                .authorizeHttpRequests((requests) -> requests
                        .requestMatchers("/home").authenticated() // Требует входа для доступа к /home
                        .anyRequest().permitAll() // Остальные страницы доступны всем
                )
                .formLogin((form) -> form
                        .loginPage("/login") // Страница входа
                        .defaultSuccessUrl("/home", true) // Перенаправление на главную после успешного входа
                        .permitAll()
                )
                .logout((logout) -> logout.permitAll()); // Обработка выхода
        return http.build();
    }
}
