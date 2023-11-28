#include "lists.h"
/**
 * check_cycle- function to check if a singly
 * lonked list has a cycle in it
 * @list: list to be checked
 * Return: 0 for no cycle and 1 if there is s cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *i, *j;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	i = list->next;
	j = list->next->next;
	while (i && j && j->next)
	{
		if (i == j)
		{
			return (1);
		}
		i = i->next;
		j = j->next->next;
	}
	return (0);
}
