#include "lists.h"
/**
 * reversing_listint - reverses a linked list
 * @head: pointer to first node in the list
 * Return: pointer to first node in the new list
 */
void reversing_listint(listint_t **head)
{
	listint_t *prv = NULL;
	listint_t *crnt = *head;
	listint_t *nxt = NULL;

	while (crnt)
	{
		nxt = crnt->nxt;
		crnt->nxt = prv;
		prv = crnt;
		crnt = nxt;
	}
	*head = prv;
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to linked list
 * Return: 1 if true, else 0 
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *tmp = *head, *dp = NULL;

	 if (*head == NULL || (*head)->nxt == NULL)
	 {
		 return (1);
	 }
	 while (1)
	 {
		 f = f->nxt->nxt;
	 }
	 if (!f)
	 {
		 dp = s->nxt;
		 break;
	 }
	 if (!f->nxt)
	 {
		 dp = s->nxt->nxt;
		 break;
	 }
	 s = s->nxt;
}
reversing_listint(&dp);
while (dp && tmp)
{
	if (tmp-> == dp->n)
	{
		dp = dp->nxt;
		tmp = tmp->nxt;
	}
	else
	{
		return (0);
	}
	if (!dp)
	{
		return (1);
	}
	return (0);
}


