{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ratm123/03MAIR---Algoritmos-de-Optimizacion---2019/blob/master/AG1/Test_sort.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NRvKNUJVQ-tv",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 170
        },
        "outputId": "0d70853a-1eae-4429-bb2b-6f1d1ea8675c"
      },
      "source": [
        "!pip install sorting"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting sorting\n",
            "  Downloading https://files.pythonhosted.org/packages/5a/a7/97e31ce3b9c16f1041bb94063a2778b666ef8ee5862094c248e9445c454c/sorting-1.0.3.tar.gz\n",
            "Building wheels for collected packages: sorting\n",
            "  Building wheel for sorting (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for sorting: filename=sorting-1.0.3-cp36-none-any.whl size=5882 sha256=ffbb86f0dd53af84b5c2a657fcb8321f0df548447502fa0d99710969cf086742\n",
            "  Stored in directory: /root/.cache/pip/wheels/eb/f9/9d/ea128e53c92937b3f10b15f961f100068615df83d0b7c3affc\n",
            "Successfully built sorting\n",
            "Installing collected packages: sorting\n",
            "Successfully installed sorting-1.0.3\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ziJsKMewRJr-",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "d8c6cfb8-60dd-4a56-983c-97c29e7e2289"
      },
      "source": [
        "import sorting\n",
        "lista = [1,3,4,7,2,10]\n",
        "ordenada = sorting.bubble(lista)\n",
        "print(ordenada)"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1, 2, 3, 4, 7, 10]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BQip4F96Rch5",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "7354d41a-615b-40c1-ad6c-f0b689557652"
      },
      "source": [
        "sorting.nextSort(lista)"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[1, 2, 3, 4, 7, 10]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "P0yT586yRmWo",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}