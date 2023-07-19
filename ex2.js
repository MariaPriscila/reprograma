db.user.aggregate(
    [
        {
          $project:
            {
              name: true,
              _id: false,
              "address.city": true,
              pets: true,
            },
        },
      ]
)
