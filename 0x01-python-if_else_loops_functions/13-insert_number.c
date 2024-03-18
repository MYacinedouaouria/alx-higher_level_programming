#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *insert_node - inserts a number into a sorted singly linked list
 *@head: a pointer to a pointer to the head of a singlu linked list
 *@number: the number to be inserted
 *Return: the address of the new node , or NULL if it fail
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;
	if (current == NULL)
	{
		*head = new;
		return (new);
	}
	else
	{
		while (current->next != NULL)
		{
			if (number >= current->n && number <= current->next->n)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			current = current->next;
		}
		current->next = new;
		return (new);
	}
}
