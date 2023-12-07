#include "lists.h"
/**
 * _palindrome- code to find palindrome
 * @num: number to check palindrome
 * Return: palindrome
 */
int _palindrome(int num)
{
	int r = 0;
	int og = num;

	while (num > 0)
	{
		int r = num % 10;
		r = r * 10 + r;
		num /= 10;
	}
	return (og == r);
}
/**
 * main- code entry point
 * Return: palindrome
 */
int main()
{
	int x, y, product, l = 0;

	for (x = 100; x < 1000; x++)
	{
		for (y = x; y < 1000; y++)
		{
			product = x * y;
			if (_palindrome(product) && product > l)
			{
				l = product;
			}
		}
	}
	printf("The largest palindrome from two 3 digit product is %d\n", l);
	return (0);
}



