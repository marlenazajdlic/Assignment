Feature: Tematy feature
  As a O2 user I would like to see selected category



  Scenario Outline: Displaying of category
    Given the homepage is loaded
    When I select "<category>" from available categories
    Then I am able to see all topics from "<stream>"

   Examples: Displayed
    | category          | stream            |
    | Hot               | hot               |
    | News              | news              |
    | Pudelek           | pudelek           |
    | Humor             | humor             |
    | Sport             | sport             |
    | Pieniądze         |pieniadze          |
    | Moto              | moto              |
    | Tech              | tech              |
    | Podróże           | podroze           |
    | Film              | film              |
    | Moda & Beauty     | moda-i-beauty     |
    | Gotowanie         | gotowanie         |
    | Gwiazdy internetu | gwiazdy-internetu |
    | Zdrowie           | zdrowie           |
    | Psychologia       | psychologia       |


  Scenario Outline: Removing stream form displayed
    Given the homepage is loaded
    When I click Plus button
    Then I am able to see all categories
    When I click "<topic>"
    And I click Zapamiętaj
    Then "<topic>" is not displayed anymore at list of available categories

   Examples:
    | topic |
    | Gwiazdy internetu |
    | Moda & Beauty     |
    | Sport             |
    | Film              |
