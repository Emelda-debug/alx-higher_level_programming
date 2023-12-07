#include "lists.h"
/**
 * insert_dnodeint_at_index- function that adds a new node at given position
 * of a dlistint_t list
 * @h: double pointer to head
 * @idx: index where node will be added
 * @n: value of node to be added
 * Return: new node address or NULL for failure
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *new_node = NULL;
	dlistint_t *head;
	unsigned int x;

	if (idx == 0)
	{
		new_node = add_dnodeint(h, n);
	}
	else
	{
		head = *h;
		x = 1;
		if (head != NULL)
		{
			while (head->prev != NULL)
			{
				head = head->prev;
			}
		}
		while (head != NULL)
		{
			if (x == idx)
			{
				if (head->next == NULL)
				{
					new_node = add_dnodeint_end(h, n);
				}
				else
				{
					new_node = malloc(sizeof(dlistint_t));
					if (new_node != NULL)
					{
						new_node->n = n;
						new_node->next = head->next;
						new_node->prev = head;
						head->next->prev = new_node;
						head->next = new_node;
					}
				}
				break;
			}
			head = head->next;
			x++;
		}
	}
	return (new_node);
}
