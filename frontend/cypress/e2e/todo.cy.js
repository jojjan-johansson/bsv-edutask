describe('Todo functionality', () => {
  let uid
  let email

  before(function () {
    cy.fixture('user.json')
      .then((user) => {
        cy.request({
          method: 'POST',
          url: 'http://localhost:5000/users/create',
          form: true,
          body: user
        }).then((response) => {
          uid = response.body._id.$oid
          email = user.email
        })
      })
  })

  beforeEach(() => {
    cy.visit('http://localhost:3000')

    cy.contains('div', 'Email Address')
      .find('input')
      .type(email)

    cy.get('form')
      .submit()

    cy.get('h1')
      .should('contain.text', 'Your tasks')
  })

  it('R8UC1 creates a todo item', () => {
    cy.get('input[placeholder="Title of your Task"]')
      .type('My Test Task')

    cy.get('input[placeholder*="Viewkey"]')
      .type('dQw4w9WgXcQ')

    cy.contains(/create new task/i)
      .click()
  })

  it('R8UC2 creates another todo item', () => {
    cy.get('input[placeholder="Title of your Task"]')
      .type('Toggle Task')

    cy.get('input[placeholder*="Viewkey"]')
      .type('dQw4w9WgXcQ')

    cy.contains(/create new task/i)
      .click()
  })

  it('R8UC3 creates a third todo item', () => {
    cy.get('input[placeholder="Title of your Task"]')
      .type('Delete Task')

    cy.get('input[placeholder*="Viewkey"]')
      .type('dQw4w9WgXcQ')

    cy.contains(/create new task/i)
      .click()
  })

  after(function () {
    cy.request({
      method: 'DELETE',
      url: `http://localhost:5000/users/${uid}`
    })
  })
})