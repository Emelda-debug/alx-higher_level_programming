#include "lists.h"
/**
 * get_dnodeint_at_index- function that returns the nth node of
 * a dlistint_t linked list
 * @head: pointer to head of the list
 * @index: index of the node to search for
 * Return: NULL if node does not exist
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int s = 0;
	dlistint_t *temp;

	if (head == NULL)
	{
		return (NULL);
	}
	temp = head;
	while (temp)
	{
		if (index == s)
		{
			return (temp);
		}
		s++;
		temp = temp->next;
	}
	return (NULL);
}


