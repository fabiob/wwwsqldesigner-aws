# wwwsqldesigner-aws

Complete serverless deployment for `wwwsqldesigner`, including a custom backend to save models on S3 using lambda functions.

## Required environment variables

* `STORAGE_S3_BUCKET`: the bucket in which to store the database designs. Must already exist.
* `STORAGE_S3_PREFIX`: the prefix to use when loadind and saving database designs.
* `STATICS_S3_BUCKET`: the bucket in which to read the `wwwsqldesigner` static files. Must already exist.

## Optional environment variables

* `CF_DOMAIN`: a custom domain name to use on the CloudFront distribution.
* `CF_CERT_ARN`: the ARN of an ACM certificate to use for the custom domain.

## Restricting access

The backend is secured using browser-based basic authentication. To manage users,
create a file named `users.json` on the root directory. The expected format is:

```json
{
  "user1": "sha256 hash of the password",
  "user2": "sha256 hash of the password"
}
```

After creating or updating the user list, perform a new deploy (using `npx serverless deploy -f auth`).

## How to deploy

Make sure the required environment variables are set, then:

```bash
npx serverless deploy
aws s3 sync static/ s3://$STATICS_S3_BUCKET/ --exclude '.git/*'
```

## TODO

* Add authorization.

## License

MIT
