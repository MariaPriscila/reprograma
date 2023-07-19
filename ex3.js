db.Pet.aggregate(
    [
      {
        $lookup: {
          from: 'User',
          localField: 'name',
          foreignField: 'pets',
          as: 'result'
        }
      },
      {
        $project: {
          petName: '$name',
          bride: true,
          'result.name': true,
          _id: false
        }
      },
      {
        $replaceRoot: {
          newRoot: {
            $mergeObjects: [
              { $arrayElemAt: ['$result', 0] },
              '$$ROOT'
            ]
          }
        }
      },
      { $project: { result: false } }
    ],
  );