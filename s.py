{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "name": "sq",
      "authorship_tag": "ABX9TyMJZUhYNNwHbidMZ+zq6y5c"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Ql9PLuZ2kSFv"
      },
      "outputs": [],
      "source": [
        "k = int(input())\n",
        "\n",
        "A = [0, 0]\n",
        "for i in range(k-1):\n",
        "    A = [A, A]\n",
        "\n",
        "print(A)"
      ]
    }
  ]
}