#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *print_listint - prints all ellements of a listint_t list
 *@h:pointer to head of listint_t list
 *Return:number of nodes
 *
 *
 */
size_t	print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /*number of nodes*/

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->next);
		n++;
	}
	return (n);
}

/**
 *add_nodeint - adds a new node at the beginning of a listint_t list
 *@head:a pointer to a pointer of the start of the list
 *@n:integer to add in the new node
 *Return:address of the new element or null if it fail
 *
 *
 */
listint_t	*add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 *free_listint - frees a listint_t list
 *@head:a pointer to the head of the list to be freed
 *
 *
 *
 *
 */
void	free_listint(listint_t *head)
{
	listint *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
