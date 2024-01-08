#include "lists.h"



listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	while (/* condition */)
	{
		
	}
	{
		/* code */
	}
	
}
