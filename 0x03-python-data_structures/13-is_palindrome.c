#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 *is_palindrome - checks if a list is a palindrome
 *@head:the list
 *Return:1 if it is a palindrome , 0 else
 *
 *
 */
int	is_palindrome(listint_t **head)
{
	int len = 0, i = 0, j;
	listint_t *l;
	listint_t *r;

	l = *head;
	r = *head;
	while (l != NULL)
	{
		len++;
		l = l->next;
	}
	if (len == 0)
		return (0);
	if (len % 2 == 0)
		j = len / 2;
	else
		j = len / 2 + 1;
	while (i < j)
	{
		r = r->next;
		i++;
	}
	l = *head;
	while (r != NULL)
	{
		if (l->n != r->n)
			return (0);
		l = l->next;
		r = r->next;
	}
	return (1);
}
