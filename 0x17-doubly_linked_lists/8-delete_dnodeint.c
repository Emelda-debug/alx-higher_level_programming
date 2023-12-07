#include "lists.h"
/**
 * delete_dnodeint_at_index- deletes the node at index index of list
 * @head: double pointer to head
 * @index: index of node to be deleted
 * Return: 1 for success, -1 for failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *x, *y;
	unsigned int i;

	x = *head;
	if (x != NULL)
	{
		while (x->prev != NULL)
		{
			x = x->prev;
		}
	}
	i = 0;
	while (x != NULL)
	{
		if (i == index)
		{
			if (i == 0)
			{
				*head = x->next;
				if (*head != NULL)
				{
					(*head)->prev = NULL;
				}
				else
				{
					y->next = x->next;
					if (x->next != NULL)
					{
						x->next->prev = y;
					}
				}
				free(x);
				return (1);
			}
			y = x;
			x = x->next;
			i++;
		}
	}
	return (-1);
}
