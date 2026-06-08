#include <iostream>
#include <random>

std::random_device rd;
std::mt19937 gen(rd());
std::uniform_real_distribution<double> dis(0.0, 1.0);

int win(int N, int i, double p) {
    if (i == 0) {
        return 0;
    }
    if (i == N) {
        return 1;
    }
    
    if (dis(gen) < p) {
        return win(N, i + 1, p);
    } else {
        return win(N, i - 1, p);
    }
}

int main() {
    int trials, N, i;
    double p;

    std::cout << "Enter number of trials: ";
    std::cin >> trials;

    std::cout << "Enter total capital on table: ";
    std::cin >> N;

    std::cout << "Enter total capital of player A: ";
    std::cin >> i;

    std::cout << "Enter prbability of A winning a round: ";
    std::cin >> p;

    int c = 0;
    for (int t = 0; t < trials; t++) {
        c += win(N, i, p);
    }

    std::cout << "A won: " << c << " out of " << trials 
              << " times; prob=" << static_cast<double>(c) / trials << "\n";

    return 0;
}