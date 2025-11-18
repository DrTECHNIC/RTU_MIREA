#include <iostream>
#include <thread>
#include <string>

// Функция для проверки сигналов
bool checkSafety(bool true_signal, bool false_signal1, bool false_signal2) {
    int activeCount = (true_signal ? 1 : 0) + (false_signal1 ? 1 : 0) + (false_signal2 ? 1 : 0);
    if (activeCount != 1)
        throw std::runtime_error("КОНФЛИКТ СОСТОЯНИЙ! Активно сигналов: " + std::to_string(activeCount));
    return true;
}

int main() {
    setlocale(LC_ALL, "Russian");
    std::cout << "Светофор запущен" << std::endl;
    std::cout << "Цикл: Красный -> Зеленый -> Желтый -> Красный..." << std::endl;
    std::cout << "Временные интервалы: Красный = 30 сек., Желтый = 5 сек., Зеленый = 30 сек." << std::endl;
    std::cout << std::endl;
    bool RLight = false; int RTime = 30;
    bool YLight = false; int YTime = 5;
    bool GLight = false; int GTime = 30;
    try {
        while (true) {
            YLight = false;
            RLight = true;
            if (checkSafety(RLight, YLight, GLight)) {
                std::cout << "Красный" << std::endl;
                std::this_thread::sleep_for(std::chrono::seconds(RTime));
            }
            RLight = false;
            GLight = true;
            if (checkSafety(GLight, RLight, YLight)) {
                std::cout << "Зеленый" << std::endl;
                std::this_thread::sleep_for(std::chrono::seconds(GTime));
            }
            GLight = false;
            YLight = true;
            if (checkSafety(YLight, GLight, RLight)) {
                std::cout << "Желтый" << std::endl;
                std::this_thread::sleep_for(std::chrono::seconds(YTime));
            }
        }
    }
    catch (const std::exception& e) {
        std::cerr << "ОШИБКА БЕЗОПАСНОСТИ: " << e.what() << std::endl;
        return 1;
    }
    catch (...) {
        std::cerr << "Неизвестная ошибка" << std::endl;
        return 1;
    }
    return 0;
}
