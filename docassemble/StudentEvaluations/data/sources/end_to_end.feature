@end_to_end
Feature: Parent requests complete student records

  # Seeded with ALDashboard's static fixture generator, then reviewed against the interview.
  Scenario: Complete the interview and reach its final document screen
    Given I start the interview at "massachusetts_entire_student_record_request.yml"
    And the maximum seconds for each Step in this Scenario is 240
    And the user gets to "download educational_evaluations_entire_record_request" with this data:
      | var | value |
      | requestor.name.first | Jane |
      | requestor.name.last | Smith |
      | requestor.address.address | 123 Main Street |
      | requestor.address.city | Boston |
      | requestor.address.state | MA |
      | requestor.address.zip | 02108 |
      | requestor.language | English |
      | requestor.right_to_send | Parent |
      | requestor.phone_number | 6175551212 |
      | requestor.email | jane@example.com |
      | student.name.first | Alex |
      | student.name.last | Smith |
      | student.birthdate | 01/02/2015 |
      | student.grade | 5th |
      | student.language | English |
      | school.address.address | 123 Main Street |
      | school.address.city | Boston |
      | school.address.state | MA |
      | school.address.zip | 02108 |
      | school.address.name | Sample Elementary School |
      | knows_special_education_director_or_coordinator_name | True |
      | school.special_education_director_or_coordinator.name.first | Casey |
      | school.special_education_director_or_coordinator.name.last | Jones |
      | school.special_education_director_or_coordinator.email | principal@example.com |
      | knows_special_education_director_name | True |
      | school.special_education_director.name.first | Casey |
      | school.special_education_director.name.last | Jones |
      | student.years_enrolled | 3 |
      | signature_choice | typed_signature |
    Then I should see the phrase "All done"
