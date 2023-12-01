#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
*add_nodeint - adds a new node at the beginning
*@head: head of listint_t
*@n: int to add in listint_t 
*Return: address of the new element, or NULL if it failed
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *newList;

	newList = malloc(sizeof(listint_t));
	if (newList == NULL)
		return (NULL);
	newList->n = n;
	newList->next = *head;
	*head = newList;
	return (newList);
}
/**
*is_palindrome - check if a syngle linked list is palindrome
*@head: head of listint_t
*Return: 1 if it is true else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *headNew = *head;
	listint_t *aux = NULL, *aux2 = NULL;

	if (*head == NULL || headNew->next == NULL)
		return (1);
	while (headNew != NULL)
	{
		add_nodeint(&aux, headNew->n);
		headNew = headNew->next;
	}
	aux2 = aux;
	while (*head != NULL)
	{
		if ((*head)->n != aux2->n)
		{
			free_listint(aux);
			return (0);
		}
		*head = (*head)->next;
		aux2 = aux2->next;
	}
	free_listint(aux);
	return (1);
}
