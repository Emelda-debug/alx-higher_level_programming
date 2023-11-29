#include"lists.h"
/**
 * insert_node- function that inserts a number into
 * a sorted singly linked list
 * @head: pointer to the head
 * @number: number to be inserted
 * Return: NULL if function fails or
 * pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *i = *head, *nw;

	nw = malloc(sizeof(listint_t));
	if (nw == NULL)
	{
		return (NULL);
	}
	nw->n = number;
	if (i == NULL || i->n >= number)
	{
		nw->next = i;
		*head = nw;
		return (nw);
	}
	while (i && i->next && i->next->n<number)
	{
		i = i->next;

		nw->next = i->next;
		i->next = nw;
	}
	return (nw);
}


