

int main() {
    float numero1, numero2, resultado;
    char causa[20], n1[20];

    printf("Digite o primeiro numero: ");
    scanf("%f", &numero1);
    printf("Digite o segundo numero: ");
    scanf("%f", &numero2);

    while (1) {
        printf("soma, subtração, divisão, multiplicação\n");
        printf("Qual operação você gostaria de realizar? ");
        scanf("%s", causa);

        if (strcmp(causa, "soma") == 0) {
            resultado = numero1 + numero2;
        } else if (strcmp(causa, "subtração") == 0) {
            resultado = numero1 - numero2;
        } else if (strcmp(causa, "divisão") == 0) {
            resultado = numero1 / numero2;
        } else if (strcmp(causa, "multiplicação") == 0) {
            resultado = numero1 * numero2;
        } else {
            printf("Operação inválida! Por favor, tente novamente.\n");
            continue;
        }

        printf("O resultado da operação é: %.2f\n", resultado);

        printf("Deseja trocar os números? (sim/não): ");
        scanf("%s", n1);
        if (strcmp(n1, "não") == 0) {
            break;
        } else if (strcmp(n1, "sim") == 0) {
            printf("Qual o novo primeiro número? ");
            scanf("%f", &numero1);
            printf("Qual o novo segundo número? ");
            scanf("%f", &numero2);
        }
    }

    return 0;
}
