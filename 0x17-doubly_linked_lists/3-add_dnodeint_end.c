#include "lists.h"
/**
 * add_dnodeint_end- function that adds a new node at the end
 * of a dlistint_t list
 * @head: double pointer to head
 * @n: value of node to be added
 * Return: new element or NULL for failure
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node;
	dlistint_t *h;

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = n;
	new_node->next = NULL;
	h = *head;
	if (h != NULL)
	{
		while (h->next != NULL)
		{
			h = h->next;
		}
		h->next = new_node;
	}
	else
	{
		*head = new_node;
	}
	new_node->prev = h;
	return (new_node);
}


