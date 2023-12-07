#include "lists.h"
/**
 * print_dlistint- function that prints all the elements
 * of a dlistint_t list
 * @h: pointer to head
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *crnt = h;
	size_t count = 0;

	while (crnt != NULL)
	{
		printf("%d\n", crnt->n);
		crnt = crnt->next;
		count++;
	}
	return (count);
}
